from testcontainers.redis import RedisContainer

if __name__ == '__main__':
    print("starting")

    with RedisContainer("redis:6.2.6-alpine") as redisContainer:
        redisClient = redisContainer.get_client().client()
        before = redisClient.exists("foo")

        # Doesn't exist before
        print(f"Exist before? {bool(before)}")

        redisClient.set("foo", "bar")

        after = redisClient.exists("foo")

        # Does exist after
        print(f"Exist after? {bool(after)}")

        value = redisClient.get("foo")

        print(f"Value after set: {value.decode()}")
