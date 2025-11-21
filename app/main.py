class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_list: list) -> list:
    """
    Creates and links Person instances based on a list of dictionaries.
    Each dictionary describes a person and may contain references to a
    wife or husband by name. All Person objects are created first, and
    then marital relationships are established using the shared registry
    Person.people.

    :param people_list: list of dictionaries describing people. Each dict
     must contain "name" and "age", and may include "wife" or "husband"
     mapped to another persons name.
    :return: list of fully initialized Person instances with correctly
     assigned spouse references where applicable
    """
    person_dict = {
        person.get("name"): Person(person.get("name"), person.get("age"))
        for person in people_list
    }

    for person in people_list:
        if person.get("wife"):
            person_dict[person.get("name")].wife = Person.people.get(
                person.get("wife")
            )

        if person.get("husband"):
            person_dict[person.get("name")].husband = Person.people.get(
                person.get("husband")
            )

    return list(person_dict.values())
