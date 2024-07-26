import json

from api.db.db_models import Log
from api.db.services.common_service import CommonService


class LogService(CommonService):
    model = Log

    @classmethod
    def save(cls, **kwargs):
        _kwargs = dict()
        for k, v in kwargs.items():
            try:
                _kwargs[k] = json.dumps(v, ensure_ascii=False, check_circular=False)
            except:
                _kwargs[k] = 'Not Json serializable'
        super().save(**kwargs)
