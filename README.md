# mysql-replication-monitor
A Python MySQL Replication Monitor with Slack and Email notifications

## How to use

Rename `config.yml.template` to `config.yml` and update the values as per your configuration.

Then you need to schedule the following command to run every 5 minutes:
```
python run.py
```

Example cron tab entry:
```
*/5 * * * * python /path/to/repo/mysql-replication-monitor/run.py
```

## TODO:
Check the issues page.


## License:
MIT
