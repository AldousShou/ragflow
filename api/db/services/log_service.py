import json

from api.db.db_models import Log
from api.db.services.common_service import CommonService


class LogService(CommonService):
    model = Log
