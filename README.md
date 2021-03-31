# Graphene Django Project

This example project demonstrate an integration between Graphene and Django.

First you'll need to get the source of the project. Do this by cloning this repository:



## Create your local environment

### There are three options here:

#### Create a Conda Environment
```bash
conda create -n graphql python=3.7 anaconda # Create the environment
source activate graphql # Activate the environment
```

#### Use the computers global python3

`Locally setup python3.7`

#### Create a Pipenv Environment (Recommended)
```bash
pipenv --python 3.7
```
Note: if you do this prefix all the following commands with `pipenv run`



## Install dependencies

#### Conda or Global
```bash
pip3 install -r requirements.txt
```

#### Pipenv
```bash
pipenv install -r requirements.txt
```



## Create database table

#### Conda or Global
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Pipenv
```bash
pipenv run python3 manage.py makemigrations
pipenv run python3 manage.py migrate
```


## Start the application

#### Conda or Global
```bash
python3 manage.py runserver
```

#### Pipenv
```bash
pipenv run python3 manage.py runserver
```


## Seeding your local Database


To seed an example run the following graphql mutation

```graphql
mutation {
  createPet(age: 5, name:"Diesel"){
    name
    age
  }
  createTree(age: 4, name: "Timber", treeType: PINE){
    name
    age
  }
  createIsland(name: "Utopia", trees: "Timber"){
    name
  }
  createPlayer(name:"Nancy", age: 7, pets: ["Diesel"], islands: ["Utopia"]){
    name
    age
  }
}
```


## Query data through GraphQL

Go to [localhost](http://localhost:8000/graphql/) on [Insomnia](https://insomnia.rest/download/#mac)
or your favorite browser to Create/Search/Filter data through GraphQL. More detail on how to write your first
query and mutation could be found [here](https://www.moesif.com/blog/technical/graphql/Getting-Started-with-Python-GraphQL-Part1/).

Example Query
```graphql
query{
  pets{
    name
    age
  }
  trees{
    name
    age
    treetype
  }
  islands{
    name
    trees{
      name
    }
  }
  players{
    name
    age
    islands{
      name
      trees{
        name
      }
    }
    pets{
      name
    }
  }
}
```

## Credits

This Project has been modeled off of the standard django example that can be found here:
https://github.com/Moesif/moesif-graphene-django-example
