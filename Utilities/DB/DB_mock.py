# This module is a mock of the database. It is used to test the functions in the Route_aggregation.py module.
# Mocking will be performed using Pandas DataFrames.
# The data will be stored in a CSV file.
# The data will be read from the CSV file and converted to a DataFrame. After the data is manipulated, it will be converted back to a CSV file.
# The DB will be used to store User data

import pandas as pd
import numpy as np
from typing import List
from DataModels.UserModel import User
import random

class DB:
    def __init__(self):
        self.users = pd.read_csv("DataModels/Users.csv")
        self.users.set_index("id_key", inplace=True)
        self.users.index = self.users.index.astype(int)
        self.users.sort_index(inplace=True)
        try:
            self.users.drop(columns=["Unnamed: 0"], inplace=True)
        except KeyError:
            pass

    def get_user(self, id_key: int) -> User:
        user = self.users.loc[id_key]
        return User(id_key=id_key, **user.to_dict())

    def add_user(self, user: User):
        self.users = self.users.append(user.to_dict(), ignore_index=True)
        self.users.to_csv("DataModels/Users.csv")

    def update_user(self, user: User):
        self.users.loc[user.id_key] = user.dict()
        self.users.to_csv("DataModels/Users.csv")

    def get_all_users(self) -> List[User]:
        users_list = []
        for i in self.users.index:
            users_list.append(User(**self.users.loc[i].to_dict()))
        return users_list

    def delete_user(self, id_key: int):
        self.users.drop(index=id_key, inplace=True)
        self.users.to_csv("DataModels/Users.csv")

    def get_user_by_username(self, username: str) -> User:
        user = self.users[self.users["username"] == username]
        return User(**user.to_dict())

    def get_user_by_fullname(self, fullname: str) -> User:
        user = self.users[self.users["fullname"] == fullname]
        return User(**user.to_dict())

    def get_user_by_age(self, age: int) -> User:
        user = self.users[self.users["age"] == age]
        return User(**user.to_dict())

    def get_user_by_rank(self, rank: int) -> User:
        user = self.users[self.users["rank"] == rank]
        return User(**user.to_dict())

    def get_user_by_current_score(self, current_score: float) -> User:
        user = self.users[self.users["current_score"] == current_score]
        return User(**user.to_dict())



def initialise_users(create_mock_users: bool = False):
    # This function will initialise the users DataBase CSV file
    users = pd.DataFrame(columns=["id_key", "username", "password", "fullname", "age", "rank", "current_score", "tokens", "total_completed_trips"])
    if create_mock_users:
        # Hand write 10 mock users with elaborated data one by one, with made up data:
        users = users.append({"id_key": 0, "username": "user0", "password": "pass0", "fullname": "User 0", "age": 20, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 5, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 1, "username": "user1", "password": "pass1", "fullname": "User 1", "age": 21, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 10, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 2, "username": "user2", "password": "pass2", "fullname": "User 2", "age": 22, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 235, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 3, "username": "user3", "password": "pass3", "fullname": "User 3", "age": 23, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 14, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 4, "username": "user4", "password": "pass4", "fullname": "User 4", "age": 24, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 90, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 5, "username": "user5", "password": "pass5", "fullname": "User 5", "age": 25, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 8, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 6, "username": "user6", "password": "pass6", "fullname": "User 6", "age": 26, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 0, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 7, "username": "user7", "password": "pass7", "fullname": "User 7", "age": 27, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 15, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 8, "username": "user8", "password": "pass8", "fullname": "User 8", "age": 28, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 100, "total_completed_trips": 0}, ignore_index=True)
        users = users.append({"id_key": 9, "username": "user9", "password": "pass9", "fullname": "User 9", "age": 29, "rank": random.randrange(1,5), "current_score": random.randrange(0,100), "tokens": 29, "total_completed_trips": 0}, ignore_index=True)

        
    users.to_csv("DataModels/Users.csv")
