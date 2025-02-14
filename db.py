import duckdb

con = duckdb.connect(database="screenshots.db")

''' FOR DEBUGGING:
# Check if the topics table exists
if con.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='topics'").fetchone()[0] == 0:

    # create the topics table
    con.execute("CREATE TABLE topics (id INTEGER PRIMARY KEY, label TEXT)")

    # Fetch the maximum topic_id from the topics table
    max_topic_id = con.execute('SELECT MAX(id) FROM topics').fetchone()[0]

    # Start the topic_id sequence from the maximum value + 1
    start_topic_id = max_topic_id + 1 if max_topic_id is not None else 1
    con.execute(f'CREATE SEQUENCE topic_id_seq START {start_topic_id}')

topics = [
    ("programming",),
    ("fitness",),
    ("psychology",),
]

# Insert topics into the topics table
for topic in topics:
    con.execute("INSERT INTO topics (id, label) VALUES (nextval('topic_id_seq'), ?)", topic)


# Check if the contents table exists
if con.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='contents'").fetchone()[0] == 0:
    # create the contents table
    con.execute("CREATE TABLE contents (id INTEGER PRIMARY KEY, topic_id INTEGER, value TEXT)")

    # Fetch the maximum value_id from the contents table
    max_value_id = con.execute('SELECT MAX(id) FROM contents').fetchone()[0]

    # Start the value_id sequence from the maximum value + 1
    start_value_id = max_value_id + 1 if max_value_id is not None else 1
    con.execute(f'CREATE SEQUENCE value_id_seq START {start_value_id}')

contents = [
    ('programming', 'Python'),
    ('programming', 'Java'),
    ('fitness', 'Running'),
    ('fitness', 'Weightlifting'),
    ('psychology', 'Cognitive Behavioral Therapy'),
]

# adds the content automatically by using topic_name instead of topic_id for automation (NLP ready)
for topic_label, content in contents:
    topic_id = con.execute("SELECT id FROM topics WHERE label = ?", [topic_label]).fetchone()[0]
    con.execute("INSERT INTO contents (id, topic_id, value) VALUES (nextval('value_id_seq'), ?, ?)", (topic_id, content))

# REMOVES duplicate topic_names from topics table because I mistakenly inserted the same topic names
# Check if the topics table exists
if con.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='topics'").fetchone()[0] > 0:
    # Remove duplicate topic names from the topics table
    con.execute("""
        DELETE FROM topics WHERE id NOT IN (
            SELECT MIN(id) FROM topics GROUP BY label
        )
    """)

    print("Duplicate topic names have been removed.")
else:
    print("The topics table does not exist in the database.")

'''

def add_content(content):
    topic_label, value = content
    # Check if the topic exists in the topics table
    result = con.execute("SELECT id FROM topics WHERE label = ?", [topic_label]).fetchone()
    if result is None:
        # If the topic does not exist, insert it into the topics table
        con.execute("INSERT INTO topics (id, label) VALUES (nextval('topic_id_seq'), ?)", [topic_label])

        # Retrieve the newly created topic_id
        topic_id = con.execute("SELECT MAX(id) FROM topics").fetchone()[0]
    else:
        # If the topic exists, retrieve its topic_id
        topic_id = result[0]

    # Insert the content into the contents table
    con.execute("INSERT INTO contents (id, topic_id, value) VALUES (nextval('value_id_seq'), ?, ?)", (topic_id, value))

    '''
    # adds the content automatically by using topic_name instead of topic_id for automation (NLP ready)
    topic_id = con.execute("SELECT id FROM topics WHERE label = ?", [topic_label]).fetchone()[0]
    con.execute("INSERT INTO contents (id, topic_id, value) VALUES (nextval('value_id_seq'), ?, ?)", (topic_id, value))
    '''

mycontent = ("masonry", "house made of concrete")
#add_content(mycontent)

# Fetch and print the content by topic
topics_result = con.execute('SELECT * FROM topics').fetchall()
for topic_row in topics_result:
    topic_id = topic_row[0]
    topic_label = topic_row[1]

    print(f"ID: {topic_id} Topic: {topic_label}")

    contents_result = con.execute('SELECT value FROM contents WHERE topic_id = ?', [topic_id]).fetchall()
    for content_row in contents_result:
        content = content_row[0]
        print(f"- {content}")

    print()  # Empty line between topics


con.close()