# multi-mcp-langchain
複数のMCP（Model Context Protocol）サーバに対応したLangChainエージェント
動いた～から一旦上げるかでやってます。

設定
---
### 関連ライブラリのインストール

```
$ pip install -r requirements.txt
```
### .envを作成
```
(Mac
$ cp .env.example .env

(Win
$ copy .env.example .env
```

### .envをよしなに埋める

Notionはインテグレーション設定とか必要

[Notion](https://www.notion.com/ja/help/create-integrations-with-the-notion-api)

[SerpApi](https://serpapi.com/manage-api-key)

```
.env

# mcp_server.pyで主に使用する
OPENAI_API_KEY=sk-XXXX
NOTION_TOKEN=ntn_XXXX
SERPAPI_API_KEY=XXXX
```

### 実行（実行前に備考↓を確認）
```
$ python main.py
```


## 備考
実行プロンプトはデフォルトで "Notionのページ一覧を出して"（NotionMCP動作確認）となっている。
適宜いい感じに修正してください。
```
main.py

        # プロンプト実行
        response = await agent.ainvoke(
            {
                "messages": "Notionのページ一覧を出して"
            }
        )
```

