import pytest
from main import get_pres_names

search_results = []

president_names = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe',
                   'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk',
                   'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
                   'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur',
                   'Cleveland', 'Harrison', 'Cleveland', 'McKinley',
                   'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge',
                   'Hoover', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson',
                   'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton',
                   'Obama', 'Trump', 'Biden']


@pytest.fixture(scope="session", autouse=True)
def setup_module():
    global search_results
    search_results = get_pres_names()
    print("Searched DuckDuckGo! This should only happen once!")


@pytest.fixture(scope="function", params=president_names)
def test_pres_name(request):
    return request.param


def test_president(test_pres_name):
    pres_found = False
    for result in search_results:
        if result.find(test_pres_name) != -1:
            pres_found = True
            break
    assert pres_found
