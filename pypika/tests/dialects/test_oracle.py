import unittest

from pypika import OracleQuery, Table
from pypika.analytics import Count


class SelectTests(unittest.TestCase):
    def test_groupby_alias_False_does_not_group_by_alias_with_standard_query(self):
        t = Table('table1')
        col = t.abc.as_('a')
        q = OracleQuery.from_(t).select(col, Count('*')).groupby(col)

        self.assertEqual('SELECT abc a,COUNT(\'*\') FROM table1 GROUP BY abc', str(q))

    def test_groupby_alias_False_does_not_group_by_alias_when_subqueries_are_present(self):
        t = Table('table1')
        subquery = OracleQuery.from_(t).select(t.abc)
        col = subquery.abc.as_('a')
        q = OracleQuery.from_(subquery).select(col, Count('*')).groupby(col)

        self.assertEqual('SELECT sq0.abc a,COUNT(\'*\') FROM (SELECT abc FROM table1) sq0 GROUP BY sq0.abc', str(q))
