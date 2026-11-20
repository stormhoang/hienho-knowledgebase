#!/usr/bin/env node

/**
 * GA4 Data Fetcher for MoMo Web Platform
 * Supports both:
 * 1. OAuth 2.0 User Auth (Client ID & Client Secret with auto-refresh token)
 * 2. Service Account (JWT authentication via private key)
 *
 * Usage:
 *   node scripts/fetch_ga4.js --days 30
 *   node scripts/fetch_ga4.js --start 30daysAgo --end yesterday
 *   node scripts/fetch_ga4.js --prefix /ve-xem-phim
 */

const fs = require("fs");
const path = require("path");
const http = require("http");
const crypto = require("crypto");
const { exec } = require("child_process");

// Configuration SSOT
const PROPERTY_ID = "270743103";
const KEY_PATHS = [
  path.join(__dirname, "..", "07_REPORTS", "data", "credentials", "ga4-credentials.json"),
  path.join(__dirname, "..", "07_REPORTS", "data", "ga4-credentials.json"),
  path.join(__dirname, "..", "07_REPORTS", "data", "credentials", "gsc-credentials.json"),
  "C:\\Users\\hien.ho\\Downloads\\momo-web-platform-seo-20fb7568b499.json"
];

function resolveKeyFile() {
  for (const p of KEY_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error(`Credentials file not found in paths: ${KEY_PATHS.join(", ")}`);
}

function base64UrlEncode(str) {
  return Buffer.from(str).toString("base64url");
}

// 1. Service Account JWT Flow
async function getServiceAccountToken(key) {
  const now = Math.floor(Date.now() / 1000);
  const header = { alg: "RS256", typ: "JWT" };
  const claim = {
    iss: key.client_email,
    scope: "https://www.googleapis.com/auth/analytics.readonly",
    aud: "https://oauth2.googleapis.com/token",
    exp: now + 3600,
    iat: now
  };

  const tokenPayload = `${base64UrlEncode(JSON.stringify(header))}.${base64UrlEncode(JSON.stringify(claim))}`;
  const sign = crypto.createSign("RSA-SHA256");
  sign.update(tokenPayload);
  const signature = sign.sign(key.private_key, "base64url");
  const jwt = `${tokenPayload}.${signature}`;

  const res = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=${jwt}`
  });
  const data = await res.json();
  if (!data.access_token) {
    throw new Error(`Failed to get OAuth token from service account: ${JSON.stringify(data)}`);
  }
  return data.access_token;
}

// 2. OAuth 2.0 User Auth Flow
async function getOAuthUserToken(creds, credsDir) {
  const clientId = creds.client_id;
  const clientSecret = creds.client_secret;
  const tokenFile = path.join(credsDir, "ga4-token.json");

  // Check existing refresh token
  if (fs.existsSync(tokenFile)) {
    try {
      const savedToken = JSON.parse(fs.readFileSync(tokenFile, "utf8"));
      if (savedToken.refresh_token) {
        const refreshParams = new URLSearchParams({
          client_id: clientId,
          client_secret: clientSecret,
          refresh_token: savedToken.refresh_token,
          grant_type: "refresh_token"
        });
        const res = await fetch("https://oauth2.googleapis.com/token", {
          method: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          body: refreshParams.toString()
        });
        const data = await res.json();
        if (data.access_token) {
          return data.access_token;
        }
      }
    } catch (e) {
      // Token expired or invalid, re-auth
    }
  }

  // Interactive Authorization
  const PORT = 8085;
  const redirectUri = `http://localhost:${PORT}`;
  const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?` + new URLSearchParams({
    client_id: clientId,
    redirect_uri: redirectUri,
    response_type: "code",
    scope: "https://www.googleapis.com/auth/analytics.readonly",
    access_type: "offline",
    prompt: "consent"
  }).toString();

  console.log(`\n======================================================`);
  console.log(`  YÊU CẦU XÁC THỰC GOOGLE ANALYTICS 4 (OAUTH 2.0)`);
  console.log(`======================================================`);
  console.log(`Vui lòng mở liên kết sau trong trình duyệt để đăng nhập tài khoản có quyền truy cập GA4 (Property: ${PROPERTY_ID}):\n`);
  console.log(authUrl);
  console.log(`\nĐang chờ xác thực từ trình duyệt trên cổng ${PORT}...`);

  // Auto-open browser on Mac/Windows
  const openCmd = process.platform === "darwin" ? `open "${authUrl}"` : process.platform === "win32" ? `start "${authUrl}"` : `xdg-open "${authUrl}"`;
  exec(openCmd, () => {});

  return new Promise((resolve, reject) => {
    const server = http.createServer(async (req, res) => {
      try {
        const reqUrl = new URL(req.url, `http://localhost:${PORT}`);
        const code = reqUrl.searchParams.get("code");
        const error = reqUrl.searchParams.get("error");

        if (error) {
          res.writeHead(400, { "Content-Type": "text/html; charset=utf-8" });
          res.end(`<h2>Xác thực thất bại: ${error}</h2>`);
          server.close();
          return reject(new Error(`OAuth Error: ${error}`));
        }

        if (code) {
          res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
          res.end(`<html><body style="font-family: -apple-system, sans-serif; text-align: center; padding: 60px;"><h2>Xác thực GA4 thành công!</h2><p>Hệ thống MoMo Web Platform đang tiến hành đồng bộ dữ liệu. Bạn có thể đóng tab này.</p></body></html>`);
          server.close();

          const tokenRes = await fetch("https://oauth2.googleapis.com/token", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({
              client_id: clientId,
              client_secret: clientSecret,
              code: code,
              grant_type: "authorization_code",
              redirect_uri: redirectUri
            }).toString()
          });

          const tokenData = await tokenRes.json();
          if (!tokenData.access_token) {
            return reject(new Error(`Failed to exchange auth code: ${JSON.stringify(tokenData)}`));
          }

          fs.writeFileSync(tokenFile, JSON.stringify({
            client_id: clientId,
            refresh_token: tokenData.refresh_token,
            updated_at: new Date().toISOString()
          }, null, 2), "utf8");

          console.log(`Xác thực thành công. Đã lưu refresh token vào: ${tokenFile}`);
          resolve(tokenData.access_token);
        }
      } catch (err) {
        reject(err);
      }
    });

    server.listen(PORT);
    server.on("error", (e) => reject(e));
  });
}

async function getAccessToken() {
  const keyFile = resolveKeyFile();
  const key = JSON.parse(fs.readFileSync(keyFile, "utf8"));
  const credsDir = path.dirname(keyFile);

  if (key.type === "service_account" || (key.client_email && key.private_key)) {
    return await getServiceAccountToken(key);
  }

  const oauthCreds = key.installed || key.web;
  if (oauthCreds && oauthCreds.client_id) {
    return await getOAuthUserToken(oauthCreds, credsDir);
  }

  throw new Error(`Định dạng credentials không hợp lệ tại ${keyFile}. Cần Service Account JSON hoặc OAuth 2.0 Client Secret.`);
}

async function runReport(accessToken, requestBody) {
  const url = `https://analyticsdata.googleapis.com/v1beta/properties/${PROPERTY_ID}:runReport`;
  const res = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(requestBody)
  });
  const data = await res.json();
  if (data.error) {
    throw new Error(`GA4 API Error: ${JSON.stringify(data.error)}`);
  }
  return data;
}

// CLI args parsing
const args = process.argv.slice(2);
function getArg(flag, defaultValue) {
  const idx = args.indexOf(flag);
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : defaultValue;
}

const hasDays30 = args.includes("--days") && getArg("--days", null) === "30" || args.includes("30");
const startDate = getArg("--start", hasDays30 ? "30daysAgo" : "30daysAgo");
const endDate = getArg("--end", "yesterday");
const prefix = getArg("--prefix", null);
const topCount = parseInt(getArg("--top", "20"), 10);

async function main() {
  const accessToken = await getAccessToken();

  console.log(`\n======================================================`);
  console.log(`  MOMO WEB PLATFORM - GA4 DATA SYNC (PROPERTY ${PROPERTY_ID})`);
  console.log(`  Khung thời gian: ${startDate} -> ${endDate}`);
  if (prefix) console.log(`  Bộ lọc URL prefix: ${prefix}`);
  console.log(`======================================================\n`);

  const dimensionFilter = prefix ? {
    filter: {
      fieldName: "pagePath",
      stringFilter: { matchType: "BEGINS_WITH", value: prefix }
    }
  } : undefined;

  // 1. Overview Metrics
  const overviewData = await runReport(accessToken, {
    dateRanges: [{ startDate, endDate }],
    metrics: [
      { name: "screenPageViews" },
      { name: "sessions" },
      { name: "activeUsers" },
      { name: "bounceRate" },
      { name: "averageSessionDuration" }
    ],
    dimensionFilter
  });

  let overviewSummary = {};
  if (overviewData.rows && overviewData.rows.length > 0) {
    const vals = overviewData.rows[0].metricValues;
    const views = Number(vals[0].value);
    const sessions = Number(vals[1].value);
    const users = Number(vals[2].value);
    const bounceRate = (Number(vals[3].value) * 100).toFixed(2);
    const avgDuration = Number(vals[4].value).toFixed(1);

    overviewSummary = {
      pageviews: views,
      sessions: sessions,
      active_users: users,
      bounce_rate_pct: Number(bounceRate),
      avg_session_duration_seconds: Number(avgDuration)
    };

    console.log(`[1. TỔNG QUAN HIỆU SUẤT TOÀN WEBSITE (30 NGÀY)]`);
    console.log(`- Pageviews        : ${views.toLocaleString("vi-VN")}`);
    console.log(`- Sessions         : ${sessions.toLocaleString("vi-VN")}`);
    console.log(`- Active Users     : ${users.toLocaleString("vi-VN")}`);
    console.log(`- Bounce Rate      : ${bounceRate}%`);
    console.log(`- Avg Duration (s) : ${avgDuration}s\n`);
  }

  // 2. Channels Breakdown (Non-Paid vs Paid)
  const channelsData = await runReport(accessToken, {
    dateRanges: [{ startDate, endDate }],
    dimensions: [{ name: "sessionDefaultChannelGroup" }],
    metrics: [
      { name: "screenPageViews" },
      { name: "sessions" },
      { name: "activeUsers" },
      { name: "bounceRate" }
    ],
    dimensionFilter,
    orderBys: [{ metric: { metricName: "screenPageViews" }, desc: true }]
  });

  const channelsSummary = [];
  if (channelsData.rows && channelsData.rows.length > 0) {
    console.log(`[2. PHÂN BỔ THEO KÊNH TRUY CẬP (TRAFFIC CHANNELS)]`);
    const totalViews = overviewSummary.pageviews || 1;
    for (const r of channelsData.rows) {
      const channel = r.dimensionValues[0].value;
      const pv = Number(r.metricValues[0].value);
      const sess = Number(r.metricValues[1].value);
      const usr = Number(r.metricValues[2].value);
      const br = (Number(r.metricValues[3].value) * 100).toFixed(2);
      const pct = ((pv / totalViews) * 100).toFixed(2);

      channelsSummary.push({
        channel,
        pageviews: pv,
        sessions: sess,
        active_users: usr,
        bounce_rate_pct: Number(br),
        share_pct: Number(pct)
      });
    }

    const formattedChannels = channelsSummary.map((c, i) => ({
      STT: i + 1,
      Channel: c.channel,
      Pageviews: c.pageviews.toLocaleString("vi-VN"),
      Tỷ_Trọng: `${c.share_pct}%`,
      Sessions: c.sessions.toLocaleString("vi-VN"),
      Users: c.active_users.toLocaleString("vi-VN"),
      BounceRate: `${c.bounce_rate_pct}%`
    }));
    console.table(formattedChannels);
    console.log("");
  }

  // 3. Top Pages
  const pagesData = await runReport(accessToken, {
    dateRanges: [{ startDate, endDate }],
    dimensions: [{ name: "pagePath" }],
    metrics: [
      { name: "screenPageViews" },
      { name: "sessions" },
      { name: "activeUsers" },
      { name: "bounceRate" }
    ],
    dimensionFilter,
    orderBys: [{ metric: { metricName: "screenPageViews" }, desc: true }],
    limit: topCount
  });

  const topPagesSummary = [];
  if (pagesData.rows && pagesData.rows.length > 0) {
    console.log(`[3. TOP ${topCount} TRANG CÓ LƯỢT XEM CAO NHẤT (LANDING PAGES)]`);
    for (const r of pagesData.rows) {
      topPagesSummary.push({
        url: r.dimensionValues[0].value,
        pageviews: Number(r.metricValues[0].value),
        sessions: Number(r.metricValues[1].value),
        active_users: Number(r.metricValues[2].value),
        bounce_rate_pct: Number((Number(r.metricValues[3].value) * 100).toFixed(2))
      });
    }

    const formattedPages = topPagesSummary.map((p, i) => ({
      STT: i + 1,
      URL: p.url,
      Pageviews: p.pageviews.toLocaleString("vi-VN"),
      Sessions: p.sessions.toLocaleString("vi-VN"),
      Users: p.active_users.toLocaleString("vi-VN"),
      BounceRate: `${p.bounce_rate_pct}%`
    }));
    console.table(formattedPages);
    console.log("");
  }

  // Save to JSON SSOT
  const outputPayload = {
    title: "MoMo Web Platform GA4 30-Day Performance Snapshot",
    property_id: PROPERTY_ID,
    synced_at: new Date().toISOString(),
    timeframe: {
      start_date: startDate,
      end_date: endDate,
      prefix_filter: prefix || "all"
    },
    overview: overviewSummary,
    channels: channelsSummary,
    top_pages: topPagesSummary
  };

  const outputPath = path.join(__dirname, "..", "07_REPORTS", "data", "ga4_30days_latest.json");
  fs.writeFileSync(outputPath, JSON.stringify(outputPayload, null, 2), "utf8");
  console.log(`[ĐỒNG BỘ HOÀN TẤT] Đã lưu dữ liệu vào: ${outputPath}\n`);
}

main().catch(err => {
  console.error("[ERROR]", err.message);
  process.exit(1);
});
