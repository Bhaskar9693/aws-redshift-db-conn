# Understanding the role of the data engineer
The role of a data engineer is to do the following:<br>
• Design, implement, and maintain the pipelines that enable the ingestion of raw data into
a storage platform<br>
• Transform that data to be optimized for analytics, based on data consumer requirements<br>
• Make that data available for various data consumers using their tool of choice<br>
<br>
The data engineer uses tools such as Apache Kafka, Apache Spark, and Presto, as well as other
commercially available products, to build the data pipeline and optimize data for analytics.

# Understanding the role of the data engineer
The role of a data engineer is to do the following:<br>
• Design, implement, and maintain the pipelines that enable the ingestion of raw data into
a storage platform<br>
• Transform that data to be optimized for analytics, based on data consumer requirements<br>
• Make that data available for various data consumers using their tool of choice<br>
<br>
The data engineer uses tools such as Apache Kafka, Apache Spark, and Presto, as well as other
commercially available products, to build the data pipeline and optimize data for analytics.

# Creating IAM user:
1. In the Search bar at the top of the screen, type in IAM and press Enter.<br>
2. This brings up the console for Identity and Access Management (IAM).<br>
3. On the left-hand side menu, click Users and then Add users.<br>
4. Provide a username, and then select the checkbox for Enable console access - optional.<br>
5. Select Custom password, provide a password for console access, select whether to force
a password change on the next login, then click Next.<br>
On the Set permissions screen, select Attach policies directly from the list of policies,
select AdministratorAccess, then click Next: Tags.<br>
6. Optionally, specify tags (key-value pairs), then click Next.<br>
7. Review the settings, and then click Create user.<br>
8. Take note of the Console sign-in URL link that you will use to sign into your account.

# Dimensional modeling in data warehouses
Data assets in the warehouse are typically stored as relational tables that are organized into
widely used dimensional models, such as a **star schema** or snowflake schema. In data warehouses, tables are generally separated into fact tables and dimension tables. The data entities are organized like a star, with the sales fact table forming the middle of the star, and the dimension tables forming the corners. The fact table also has a large number of foreign key columns that reference the primary keys of associated dimension tables.
In a star schema, while data for a subject area is normalized by splitting measurements and context information into separate fact and dimension tables, individual dimension tables are typically kept denormalized so that all related attributes of a dimensional topic can be found in a single table.
This makes it easier to find all related attributes of a dimensional topic in a single table (fewer joins, and a simpler-to-understand model), but for larger dimension tables, a denormalized approach can lead to data duplication and inconsistencies within the dimension table. Large denormalized dimension tables can also be slow to update.

The challenges of inconsistencies and duplication in a star schema can be addressed by snowflaking (basically normalizing) each dimension table into multiple related dimension tables (normalizing the original product dimension into product and product category dimensions, for example). This normalization of tables continues until each individual dimension table contains only attributes with a direct correlation with the table’s primary key. The highly normalized model resulting from this snowflaking is called a **snowflake schema**.
A snowflake schema can reduce redundancy and minimize disk space, compared to a star schema, which often contains duplicate records. However, on the other hand, the snowflake schema may necessitate complex joins to answer business queries and
may slow down query performance.




