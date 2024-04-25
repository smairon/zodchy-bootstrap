import settings
import os
import uvicorn


def run(version='v1'):
    host = os.environ.get('APP_HOST') or settings.APP_HOST
    port = int(os.environ.get('APP_PORT')) if os.environ.get('APP_PORT') else settings.APP_PORT
    workers_num = int(os.environ.get('WORKERS_NUM')) if os.environ.get('WORKERS_NUM') else settings.APP_WORKERS_NUM
    uvicorn.run(
        f"ports.api.instance:app_{version}",
        host=host,
        port=port,
        workers=workers_num,
        proxy_headers=True,
        reload=os.environ.get('RELOAD') or False,
    )
