import os
import json
from dotenv import load_dotenv

# 
# 環境変数(.env)の読み込み
# 
load_dotenv()

# 
# 使用するMCPサーバの設定
# 
def load_mcp_servers():
    return {

        # Google検索
        "google-patents-mcp": {
            "command": "npx",
            "args": ["-y", "@kunihiros/google-patents-mcp"],
            "env": {
                "SERPAPI_API_KEY": os.getenv("SERPAPI_API_KEY")
            }   
        },

        # Youtubeの動画読み込み
        "youtube": {
            "command": "npx",
            "args": ["-y", "@anaisbetts/mcp-youtube"]
        },

        # Notionの参照と操作
        "notionApi": {
            "command": "npx",
            "args": ["-y", "@notionhq/notion-mcp-server"],
            "env": {
                "OPENAPI_MCP_HEADERS": json.dumps({
                    "Authorization": f"Bearer {os.getenv('NOTION_TOKEN')}",
                    "Notion-Version": "2022-06-28"
                })
            }
        }
        
    }
