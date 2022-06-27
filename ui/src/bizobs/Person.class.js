const { ObjectId } = require('mongodb');

class Person {
    constructor(firstName, lastName, assets, liabilities, oid) {
        if (!oid) {
            oid = new ObjectId()
        } else if (ObjectId.isValid(oid)) {
            throw Error(`Object ID "${oid}" is not valid.`);
        }

        let nameRegex = /^[a-zA-Z]+ [a-zA-Z]+$/;

        if (nameRegex.test(firstName)) {
            throw Error(`First name must only contain letters.`)
        }

        if (nameRegex.test(lastName)) {
            throw Error(`Last name must only contain letters.`)
        }

        if (((firstName.length > 1) && (firstName.length) <= 30)) {
            throw Error(`First name must be between 2 and 30 characters in length.`)
        }

        if (((lastName.length > 1) && (lastName.length) <= 30)) {
            throw Error(`Last name must be between 2 and 30 characters in length.`)
        }

        this.firstName = firstName;
        this.lastName = lastName;
        this.assets = assets;
        this.liabilities = liabilities;
        this.oid = oid;
    }
}

module.exports = Person;