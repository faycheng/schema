import records
import pymysql
import codecs

codecs.register(
    lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

pymysql.install_as_MySQLdb()

db = None
dsn = None
schema = None


class SQL:
    QUERY_TABLES = "SELECT table_name, table_comment FROM information_schema.tables WHERE table_schema = '{}' AND table_type = 'BASE TABLE'"
    QUERY_FIELDS = "SELECT ordinal_position AS field_ordinal, column_name, column_comment, IF(data_type = 'enum', column_name, column_type) AS data_type, IF(is_nullable = 'YES', false, true) AS not_null, column_default AS default_value, IF(column_key = 'PRI', true, false) AS is_primary_key FROM information_schema.columns WHERE table_schema = '{}' AND table_name = '{}' ORDER BY ordinal_position"


class Field(object):
    def __init__(self, record):
        self.name = record.column_name
        self.comment = record.column_comment
        self.origin_type = record.data_type


class Table(object):
    def __init__(self, row):
        self.name = row.table_name
        self.comment = row.table_comment

    @property
    def fields(self):
        rows = db.query(SQL.QUERY_FIELDS.format(schema, self.name))
        return [Field(row) for row in rows]


class Schema(object):
    def __init__(self, dsn):
        self.dsn = dsn
        self.init_db()

    @property
    def db(self):
        return self.dsn.split("/")[-1]

    def init_db(self):
        global db, dsn, schema
        dsn = self.dsn
        schema = self.schema
        db = records.Database(self.dsn)

    @property
    def tables(self):
        rows = db.query(SQL.QUERY_TABLES.format(self.schema))
        return [Table(row) for row in rows]


