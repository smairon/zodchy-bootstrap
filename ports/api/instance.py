import settings
import os
import uvicorn
import specs

from . import v1


def launch(cqrs_factory: specs.services.CQRSFactoryContract, jwt_secret: str):
    host = os.environ.get('APP_HOST') or settings.APP_HOST
    port = int(os.environ.get('APP_PORT')) if os.environ.get('APP_PORT') else settings.APP_PORT
    workers_num = int(os.environ.get('WORKERS_NUM')) if os.environ.get('WORKERS_NUM') else settings.APP_WORKERS_NUM
    uvicorn.run(
        app=v1.bootstrap.api(cqrs_factory, jwt_secret),
        host=host,
        port=port,
        workers=workers_num,
        proxy_headers=True,  # TODO: Add X-Real-IP to nginx config
        reload=os.environ.get('RELOAD') or False,
    )
