# Indian Cities
<p>The app created will be displaying the cities of India along with the district and the state the belong to. This app makes calls to external API hosted in https://indian-cities-api-nocbegfhqg.now.sh/cities" 
 
# How it works
<p>You can check the external APIs and in-built rest services to read, add, update and delete (CRUD) the cities in the country<p>
 
 # Features
 <ol>
 <li>REST-based service interface.</li>
 <li>Interaction with external REST services.</li>
 <li>Use of on an external Cloud database(cassandra db) for persisting information.</li>
 <li>Support for cloud scalability, deployment in a container environment.</li>
 <li>Cloud security awareness by running my flask application over HTTPS Using self-signed certificate.</li>
 </ol>
 
 # Terminal Commands
 ## External API
GET ```@app.route('/cities/integrate', methods=['GET'])```
<p>Get the summary of the whole data from the actual source</p>

## REST-based Service Interface
#### GET ```1 @app.route('/cities', methods=['GET'])```
<p>Get the list of all the cities along with their district and state</p>

<p>It can be executed using the following curl command:</p>
```curl -k -v https://0.0.0.0:443/cities```

#### GET ```2 @app.route('/cities/<state>', methods=['GET'])```
<p>Get the list of cities of a given state</p>

#### POST ```3 @app.route('/cities', methods=['POST'])```
<p>To add a new city along with its state and  district</p>
<p>The user must provide:</p>

 <p>* city</p>
 <p>* district</p>
 <p>* state</p>
 
 <p>The POST request will be executed in the following way. In the following curl command, i am using "qqq" as the city with state "mmm" and the district as "uuu"</p>
 
 ```POST: curl -k -i -H "Content-Type: application/json" -X POST -d '{"city":"qqq","state":"ddd","district":"uuu"}' https://0.0.0.0:443/cities```
 

#### PUT ```4 @app.route('/cities', methods=['PUT'])```
<p> To change the name of the state and district of the given city.</p>

<p>The user must provide:</p>

 <p>* city</p>
 <p>* district</p>
 <p>* state</p>

 <p>Following is the curl command used to execute the PUT request. Here the city is "SGMA" with state "ddd" and city "uuu".
 
 ```curl -k -i -H "Content-Type: application/json" -X PUT -d '{"city":"SGM","state":"ddd","district":"uuu"}' https://0.0.0.0:443/cities"```


 #### DELETE ```@app.route('/cities/<city>', methods=['DELETE'])```
 <p>To delete a city from the database</p>
 
 <p> The user must provide the city name!</p>
 <p>THE curl command used for the DELETE request with city "www" is:</p>
 
 ```curl -k -X DELETE HTTPS://0.0.0.0:443/cities/www```
 
 ### Deployment
 
 <p>1:Initial steps</p>
 
 ```<p>sudo apt update</p>``` 
 ```<p>sudo apt install docker.io</p>```
 ```<p>sudo docker pull cassandra:latest</p>```
 
  <p>2:Run cassandra in a Docker container and expose port 9042:</p>
  
  ```sudo docker run --name cassandra-test -p 9042:9042 -d cassandra:latest```
 <p>3:Download result.csv from the tiny url created through the raw github url wchich contains the data</p>
 
 ```wget -O result.csv https://tinyurl.com/yczwx7z6```
 
 <p>4:Copy the csv file into the container</p>
 
 ```sudo docker cp result.csv cassandra-test:/home/result.csv```
 <p>5:Access the cassandra container in iterative mode:</p>
 
 ```sudo docker exec -it cassandra-cont cqlsh```
 
 <p>6:Creating a Keyspace for cities database</p>
 
 ``` cqlsh> CREATE KEYSPACE cities WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};```
 
 <p>Create the database table for the list of cities with state and district:</p>
 
```cqlsh> CREATE TABLE cities.result (city text PRIMARY KEY, state text, district text);```
 
 <p> copy the data from our csv into the database</p>

```COPY cities.result (city, state, district) FROM '/home/result.csv' WITH DELIMITER=',' AND HEADER=TRUE ```

### Security

<p>This app is served over https.</p>

<p>I have cert.pem -keyout key.pem with the code.</p>

<p>This is how I added self-signed certificate.</p>

```Self-signed certificate
Generating a 4096 bit RSA private key
.........................++
.........++
writing new private key to 'key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:UK
State or Province Name (full name) [Some-State]:LONDON
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:
```
<p>Inside app.py</p>

```
if __name__ ==  '__main__':
    app.run(host ='0.0.0.0',port = 443, ssl_context=(cert.pem,key.pem))
```
    
 <p>Adding the ceritficate will add security to our app and will now use https.</p>
 
 #### Execution
 
```cd minip/
sudo docker build . --tag=cassandrarest:v1
sudo docker run -dp 443:443 cassandrarest:v1
  ```
 
 #### Bugs and their resolution:
 
 ```If you are using MAC open the link click on the background and type "thisisunsafe". Other browser proceed anyways.```

  ### Licenese and copyright
  @SHARMILA THAKUR, Queen Mary University of London. 
  
 
 
 
    







