import React, {useState, useEffect} from 'react'
import {View, Text, Button} from 'react-native'
import styles from './styles'

export default function Home({navigation, route}){
    const [cont, setCont] = useState(0)


    return(
        <View style={styles.container}>
            <View>
                <Text style={styles.txt}></Text>
            </View>
            <View>
            
                <Text>Olá Paula</Text>
            </View>

        </View>       
    )
}
