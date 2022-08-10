import AsyncStorage from '@react-native-async-storage/async-storage';

import MySqlConnection from 'react-native-my-sql-connection';
 
let config = {
    hhost: 'wordle.ce3zuwpfpvje.us-east-1.rds.amazonaws.com',
	user: 'admin',
	password: 'Moarte01`',
	database: 'Wordle'
    };
    try{
        const connection = await MySqlConnection.createConnection(config);
        let res = await connection.executeQuery('SELECT * FROM myTable');
        connection.close();
    }catch(err){
        console.log("Error")
        // handle error
    }