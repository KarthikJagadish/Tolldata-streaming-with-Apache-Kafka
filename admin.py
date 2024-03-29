from kafka.admin import KafkaAdminClient,NewTopic

# Creating KafkaAdminClient Object
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = []

# Creating new topic
new_topic = NewTopic(name="toll", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)

admin_client.create_topics(new_topics=topic_list)
