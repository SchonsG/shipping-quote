from datetime import datetime

from pony.orm import Database, PrimaryKey, Required, db_session

from .settings import DB_SETTINGS

db = Database()


class Transporter(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    constant = Required(float)
    max_height = Required(int)
    min_height = Required(int)
    max_width = Required(int)
    min_width = Required(int)
    delivery_time = Required(int)
    active = Required(bool, default=True)
    updated_at = Required(datetime, default=datetime.utcnow())
    created_at = Required(datetime, default=datetime.utcnow())

    @classmethod
    @db_session
    def check_delivery_availability(cls, height: int, width: int) -> list:
        sql = f"""
            SELECT id, name, constant, delivery_time
            FROM {cls.__name__}
            WHERE min_height <= $height
              AND max_height >= $height
              AND min_width <= $width
              AND max_width >= $width
        """

        params = {
            "height": height,
            "width": width,
        }

        return cls.select_by_sql(sql, params)


db.bind(**DB_SETTINGS)
db.generate_mapping(create_tables=True)
