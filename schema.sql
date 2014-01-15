drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  keyword text not null,
  helptext text not null
);
