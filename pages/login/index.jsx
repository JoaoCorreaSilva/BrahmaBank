import React, { useState } from 'react'
import { View, Text, TextInput, TouchableOpacity, Image } from 'react-native'
import styles from './styles'
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from '../firebaseConfig';



export default function Login({ navigation }) {

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    

    const logar = () => {
        signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                // Signed in 
                const user = userCredential.user;
                navigation.navigate('Home', {usuario:email})
            })
            .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
            });
    }

    return (
        <View style={styles.caixas}>
          <View>
            <Image
              source={require('../../assets/logo.png')}
              style={{ width: 440, height: 100 }}
            />
          </View>
          <View>
            <TextInput
              placeholder='email'
              onChangeText={setEmail}
              value={email}
              style={styles.caixa}
            />
            <TextInput
              placeholder='password'
              onChangeText={setPassword}
              value={password}
              style={styles.caixa}
              secureTextEntry={true}
            />
      
            <TouchableOpacity
              style={styles.btnOk}
              onPress={logar}
            >
              <Text style={{ fontSize: 25 }}>Sign In</Text>
            </TouchableOpacity>
      
            <TouchableOpacity
              style={styles.btnOk}
              onPress={() => navigation.navigate('SignUp')}
            >
              <Text style={{ fontSize: 25 }}>Sign Up</Text>
            </TouchableOpacity>
          </View>
        </View>
      )
    }
