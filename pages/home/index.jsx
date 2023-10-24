import React, {useState, useEffect} from 'react'
import {View, Text, Button} from 'react-native'
import styles from './styles'

export default function Home({navigation, route}){
    const [cont, setCont] = useState(0)
    const [cont2, setCont2] = useState(0)

    useEffect(()=>{setCont2(cont2+1)}, [cont])

    return(
        <View style={styles.container}>
            <View>
                <Text style={styles.txt}></Text>
            </View>
            <View>
                <Text>Contador 1: {cont}</Text>
            </View>
            <View>
                <Text>Contador 2: {cont2}</Text>
            </View>
            <View>
                <Button
                    title='Contador1'
                    onPress={()=>setCont(cont+1)}
                    />
            </View>
            <View>
                <Button
                    title='Contador2'
                    onPress={()=>setCont2(cont2+1)}
                />
            </View>



        </View>       
    )
}
