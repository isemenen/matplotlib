from sec_api import QueryApi
queryApi = QueryApi(api_key="99d7a8dd80eb037918049221f11615110ee7d32d8c96c9480fcc1623c44b774f")

query = {
  "query": { "query_string": {
      "query": "ticker:TSLA AND filedAt:[2020-01-01 TO 2021-12-31] AND formType:\"10-K\"",
      "time_zone": "America/New_York"
  } },
  "from": "0",
  "size": "200",
  "sort": [{ "filedAt": { "order": "desc" } }]
}
response = queryApi.get_filings(query)

# ------------------------------------------------------------------------------------- #

import json
# response is a dict with multiple keys. The most important one is "filings".
# response["filings"] is a list and includes all filings returned by the Query API.
print(json.dumps(response["filings"][0], indent=2))

base_query = {
  "query": {
      "query_string": {
          "query": "PLACEHOLDER", # this will be set during runtime
          "time_zone": "America/New_York"
      }
  },
  "from": "0",
  "size": "200", # dont change this
  # sort by filedAt
  "sort": [{ "filedAt": { "order": "desc" } }]
}

log_file = open("filing_urls.txt", "a")
# start with filings filed in 2021, then 2020, 2019, ... up to 2010
# uncomment line below to fetch all filings filed in 2022-2010
# for year in range(2021, 2009, -1):
for year in range(2022, 2020, -1):
    print("starting {year}".format(year=year))

    # a single search universe is represented as a month of the given year
    for month in range(1, 13, 1):
        # get 10-Q and 10-Q/A filings filed in year and month
        # resulting query example: "formType:\"10-Q\" AND filedAt:[2021-01-01 TO 2021-01-31]"
        universe_query = \
            "formType:\"10-K\" AND " + \
            "filedAt:[{year}-{month:02d}-01 TO {year}-{month:02d}-31]" \
                .format(year=year, month=month)

        print(universe_query)
        # set new query universe for year-month combination
        base_query["query"]["query_string"]["query"] = universe_query;

        # paginate through results by increasing "from" parameter
        # until we don't find any matches anymore
        # uncomment line below to fetch 10,000 filings
        # for from_batch in range(0, 9800, 200):
        for from_batch in range(0, 400, 200):
            # set new "from" starting position of search
            base_query["from"] = from_batch;

            response = queryApi.get_filings(base_query)

            # no more filings in search universe
            if len(response["filings"]) == 0:
                break;

            # for each filing, only save the URL pointing to the filing itself
            # and ignore all other data.
            # the URL is set in the dict key "linkToFilingDetails"
            urls_list = list(map(lambda x: x["linkToFilingDetails"], response["filings"]))

            # transform list of URLs into one string by joining all list elements
            # and add a new-line character between each element.
            urls_string = "\n".join(urls_list) + "\n"

            log_file.write(urls_string)

log_file.close()