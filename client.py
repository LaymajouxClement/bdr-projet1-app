import oracledb
import configparser

class Client():
    def __init__(self, user, password) -> None:
        config = configparser.ConfigParser()
        config.read('.conf')
        self.user = user
        self.password = password

        self.db = config["DB"]
        self.host = self.db["HOST"]
        self.port = self.db["PORT"]
        self.sid = self.db["SID"]
        self.dsn = self.host+":"+self.port+"/"+self.sid

        self.path = self.db["PATH_INSTANTCLIENT"]
        oracledb.init_oracle_client(lib_dir=self.path)

    def login(self,user=None,password=None) -> bool:
        if user:
            self.user = user

        if password:
            self.password = password

        connexion = self.create_connexion()
        if connexion :
            connexion.close()
        return connexion is not None


    def create_connexion(self) -> oracledb.Connection:
        try:
            return oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
                )
        except Exception as e:
            print(e)
            return None

    def query(self,SQL_QUERY:str) -> list:
        connexion:oracledb.Connection = self.create_connexion()
        if not connexion:
            return []

        try:
            with connexion.cursor() as cursor:
                res = []
                for r in cursor.execute(SQL_QUERY):
                    res.append(r)

                # connexion.close()
                return res
        except Exception as e:
            print(e)
            return []
