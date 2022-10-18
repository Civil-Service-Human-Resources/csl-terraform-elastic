import sys
import create_tf_backend
import create_elastic_users


def run():
    args = sys.argv[1:]
    for arg in args:
        if arg == "tf_backend":
            create_tf_backend.run()
        if arg == "elastic_users":
            create_elastic_users.run()


run()
