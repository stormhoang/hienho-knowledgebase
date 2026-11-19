# -*- coding: utf-8 -*-
"""
GTM API CLIENT (SSOT)
Client dùng chung cho Google Tag Manager API v2 (service account).
Thay thế pattern copy-paste trong scratch/check_gtm_*.py, review_gtm_*.py.

Containers:
- Web Out-App: accounts/4262611053/containers/10104547 (GTM-P9JDDJZ)
- In-App:      accounts/4262611053/containers/57119568 (GTM-5TCGRPX - cần verify)

Usage:
    from scripts.lib.gtm_client import GtmClient
    c = GtmClient()  # default web container
    live = c.latest_version()
    tags = c.list_tags()
"""

import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CREDS_FILE = os.path.join(REPO_ROOT, "07_REPORTS", "data", "credentials", "gsc-credentials.json")

CONTAINER_WEB = "accounts/4262611053/containers/10104547"   # GTM-P9JDDJZ
CONTAINER_INAPP = "accounts/4262611053/containers/57119568"  # cần verify public ID

SCOPES = [
    "https://www.googleapis.com/auth/tagmanager.readonly",
    "https://www.googleapis.com/auth/tagmanager.edit.containers",
    "https://www.googleapis.com/auth/tagmanager.edit.containerversions",
    "https://www.googleapis.com/auth/tagmanager.manage.users",
    "https://www.googleapis.com/auth/tagmanager.publish",
]


class GtmClient:
    def __init__(self, container_path: str = CONTAINER_WEB, creds_file: str = CREDS_FILE):
        creds = service_account.Credentials.from_service_account_file(creds_file, scopes=SCOPES)
        self.service = build("tagmanager", "v2", credentials=creds, cache_discovery=False)
        self.container = container_path.rstrip("/")
        self._acc = self.container.split("/")[1]
        self._cont = self.container.split("/")[3]

    # ---- version ----
    def latest_version(self) -> dict:
        """Live version header: containerVersionId, name, numTags, numTriggers..."""
        return self.service.accounts().containers().version_headers().latest(
            parent=self.container).execute()

    def version_detail(self, version_id: int) -> dict:
        return self.service.accounts().containers().versions().get(
            path=f"{self.container}/versions/{version_id}").execute()

    def list_versions(self, page_size: int = 10) -> list:
        res = self.service.accounts().containers().versions().list(
            parent=self.container, pageSize=page_size).execute()
        return res.get("containerVersion", [])

    # ---- workspace ----
    def list_workspaces(self) -> list:
        res = self.service.accounts().containers().workspaces().list(parent=self.container).execute()
        return res.get("workspace", [])

    def default_workspace(self) -> dict:
        for ws in self.list_workspaces():
            if ws.get("name") == "Default Workspace":
                return ws
        return self.list_workspaces()[0]

    # ---- entities (đọc từ live version hoặc workspace) ----
    def _entities_from_version(self, kind: str) -> list:
        live = self.latest_version()
        detail = self.version_detail(live["containerVersionId"])
        return detail.get(kind, [])

    def list_tags(self, live: bool = True) -> list:
        if live:
            return self._entities_from_version("tag")
        ws = self.default_workspace()
        res = self.service.accounts().containers().workspaces().tags().list(
            parent=ws["path"]).execute()
        return res.get("tag", [])

    def list_triggers(self, live: bool = True) -> list:
        if live:
            return self._entities_from_version("trigger")
        ws = self.default_workspace()
        res = self.service.accounts().containers().workspaces().triggers().list(
            parent=ws["path"]).execute()
        return res.get("trigger", [])

    def list_variables(self, live: bool = True) -> list:
        if live:
            return self._entities_from_version("variable")
        ws = self.default_workspace()
        res = self.service.accounts().containers().workspaces().variables().list(
            parent=ws["path"]).execute()
        return res.get("variable", [])

    # ---- folders ----
    def list_folders(self) -> list:
        ws = self.default_workspace()
        res = self.service.accounts().containers().workspaces().folders().list(
            parent=ws["path"]).execute()
        return res.get("folder", [])


def get_client(container: str = "web") -> GtmClient:
    path = {"web": CONTAINER_WEB, "inapp": CONTAINER_INAPP}.get(container, container)
    return GtmClient(path)


if __name__ == "__main__":
    c = get_client("web")
    lv = c.latest_version()
    print(f"Live version: {lv.get('containerVersionId')} | {lv.get('name')} "
          f"| tags={lv.get('numTags')} triggers={lv.get('numTriggers')}")
    print(f"Workspaces: {len(c.list_workspaces())} | Folders: {len(c.list_folders())}")
    print(f"Tags (live): {len(c.list_tags())} | Triggers (live): {len(c.list_triggers())}")
    for f in c.list_folders()[:15]:
        print(f"  folder {f.get('folderId')}: {f.get('name')}")
