from database.DB_connect import DBConnect
from model.movie import Movie


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from movies m 
                    where m.`rank` is not null  """

        cursor.execute(query, ())

        for row in cursor:
            result.append(Movie(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(rank):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select m.id as m1 , m2.id as m2,count(distinct r.actor_id) as count
                    from movies m , roles r, movies m2 , roles r2 
                    where m.id = r.movie_id 
                    and m.`rank` >= %s
                    and m2.id = r2.movie_id 
                    and m2.`rank` >= %s
                    and m.id < m2.id
                    and r2.actor_id = r.actor_id
                    group by m.id, m2.id   """

        cursor.execute(query, (rank, rank))

        for row in cursor:
            result.append([row["m1"], row["m2"], row["count"]])

        cursor.close()
        conn.close()
        return result