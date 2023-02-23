# elasticSearch

In this repository we have added the elasticsearch theory with code in python.


[Official Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-analyze.html)

Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that have been serialized as JSON documents. When you have multiple Elasticsearch nodes in a cluster, stored documents are distributed across the cluster and can be accessed immediately from any node.

When a document is stored, it is indexed and fully searchable in near real-time--within 1 second. Elasticsearch uses a data structure called an inverted index that supports very fast full-text searches. An inverted index lists every unique word that appears in any document and identifies all of the documents each word occurs in.
An index can be thought of as an optimized collection of documents and each document is a collection of fields, which are the key-value pairs that contain your data. By default, Elasticsearch indexes all data in every field and each indexed field has a dedicated, optimized data structure. For example, text fields are stored in inverted indices, and numeric and geo fields are stored in BKD trees. The ability to use the per-field data structures to assemble and return search results is what makes Elasticsearch so fast.

Elasticsearch also has the ability to be schema-less, which means that documents can be indexed without explicitly specifying how to handle each of the different fields that might occur in a document. When dynamic mapping is enabled, Elasticsearch automatically detects and adds new fields to the index. This default behavior makes it easy to index and explore your data—​just start indexing documents and Elasticsearch will detect and map booleans, floating point and integer values, dates, and strings to the appropriate Elasticsearch data types.

Ultimately, however, you know more about your data and how you want to use it than Elasticsearch can. You can define rules to control dynamic mapping and explicitly define mappings to take full control of how fields are stored and indexed.

Defining your own mappings enables you to:

Distinguish between full-text string fields and exact value string fields
Perform language-specific text analysis
Optimize fields for partial matching
Use custom date formats
Use data types such as geo_point and geo_shape that cannot be automatically detected
It’s often useful to index the same field in different ways for different purposes. For example, you might want to index a string field as both a text field for full-text search and as a keyword field for sorting or aggregating your data. Or, you might choose to use more than one language analyzer to process the contents of a string field that contains user input.

The analysis chain that is applied to a full-text field during indexing is also used at search time. When you query a full-text field, the query text undergoes the same analysis before the terms are looked up in the index.
Information out: search and analyzeedit
While you can use Elasticsearch as a document store and retrieve documents and their metadata, the real power comes from being able to easily access the full suite of search capabilities built on the Apache Lucene search engine library.

Elasticsearch provides a simple, coherent REST API for managing your cluster and indexing and searching your data. For testing purposes, you can easily submit requests directly from the command line or through the Developer Console in Kibana. From your applications, you can use the Elasticsearch client for your language of choice: Java, JavaScript, Go, .NET, PHP, Perl, Python or Ruby.

Searching your dataedit
The Elasticsearch REST APIs support structured queries, full text queries, and complex queries that combine the two. Structured queries are similar to the types of queries you can construct in SQL. For example, you could search the gender and age fields in your employee index and sort the matches by the hire_date field. Full-text queries find all documents that match the query string and return them sorted by relevance—how good a match they are for your search terms.

In addition to searching for individual terms, you can perform phrase searches, similarity searches, and prefix searches, and get autocomplete suggestions.

Have geospatial or other numerical data that you want to search? Elasticsearch indexes non-textual data in optimized data structures that support high-performance geo and numerical queries.

You can access all of these search capabilities using Elasticsearch’s comprehensive JSON-style query language (Query DSL). You can also construct SQL-style queries to search and aggregate data natively inside Elasticsearch, and JDBC and ODBC drivers enable a broad range of third-party applications to interact with Elasticsearch via SQL.

Analyzing your dataedit
Elasticsearch aggregations enable you to build complex summaries of your data and gain insight into key metrics, patterns, and trends. Instead of just finding the proverbial “needle in a haystack”, aggregations enable you to answer questions like:

How many needles are in the haystack?
What is the average length of the needles?
What is the median length of the needles, broken down by manufacturer?
How many needles were added to the haystack in each of the last six months?
You can also use aggregations to answer more subtle questions, such as:

What are your most popular needle manufacturers?
Are there any unusual or anomalous clumps of needles?
Because aggregations leverage the same data-structures used for search, they are also very fast. This enables you to analyze and visualize your data in real time. Your reports and dashboards update as your data changes so you can take action based on the latest information.

What’s more, aggregations operate alongside search requests. You can search documents, filter results, and perform analytics at the same time, on the same data, in a single request. And because aggregations are calculated in the context of a particular search, you’re not just displaying a count of all size 70 needles, you’re displaying a count of the size 70 needles that match your users' search criteria—​for example, all size 70 non-stick embroidery needles.

But wait, there’s moreedit
Want to automate the analysis of your time series data? You can use machine learning features to create accurate baselines of normal behavior in your data and identify anomalous patterns. With machine learning, you can detect:

Anomalies related to temporal deviations in values, counts, or frequencies
Statistical rarity
Unusual behaviors for a member of a population
And the best part? You can do this without having to specify algorithms, models, or other data science-related configurations.
