FROM postgres:15

# add backup scripts
COPY containers/postgres/backup.sh /usr/local/bin/backup
COPY containers/postgres/restore.sh /usr/local/bin/restore
COPY containers/postgres/list-backups.sh /usr/local/bin/list-backups

# make them executable
RUN chmod +x /usr/local/bin/restore
RUN chmod +x /usr/local/bin/list-backups
RUN chmod +x /usr/local/bin/backup
