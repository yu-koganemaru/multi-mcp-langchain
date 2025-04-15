import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from mcp_servers import load_mcp_servers

# 
# 環境変数(.env)の読み込み
# 
load_dotenv()

async def run_client() -> None:

    # 
    # 使用するModelの設定
    # 
    model = ChatOpenAI(model="gpt-3.5-turbo")

    # 
    # 複数MCP対応クライアント
    # 
    async with MultiServerMCPClient(
        load_mcp_servers()
        ) as client:
        
        # ツール群の読み込み
        tools = [
            tool for tool in client.get_tools()
                if tool.name != "API-patch-block-children"
                # なんかNotion MCPのAPI-patch-block-childrenだけ形式で怒られるので一旦除外
            ]
        # tools = client.get_tools()    本来ならこれだけでOK

        # エージェント作成
        agent = create_react_agent(model, tools)

        # プロンプト実行
        response = await agent.ainvoke(
            {
                "messages": "Notionのページ一覧を出して"
            }
        )

        # レスポンスの表示
        print("Messages:")
        for msg in response['messages']:
            if isinstance(msg, AIMessage) and msg.content:
                print(msg.content)

if __name__ == "__main__":
    asyncio.run(run_client())
    