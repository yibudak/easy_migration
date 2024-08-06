dropdb -f 16migration_base
createdb 16migration_base
psql -d 16migration_base -f 16migration_base.dump
