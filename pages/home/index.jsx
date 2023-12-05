import React, { useState, useEffect } from 'react';
import { View, Text, Pressable, Image } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';
import styles from './styles';

export default function Home({ navigation, route }) {
  const [cont, setCont] = useState(0);

    return (
      <>
      <View style={styles.container}>
        <View style={styles.cima}>
          <View>
            <Icon name="user" size={40} color="black" />
          </View>
          <Text>Olá Paula</Text>
        </View>
        <View style={styles.viewBotoes}>
          <Pressable onPress={() => console.log("PIX CLICADO")}>
            <Image
              source={require('../images/pix.png')}
              style={{ width: 60, height: 60 }}
            />
          </Pressable>
          <Pressable onPress={() => console.log("CARTAO CLICADO")}>
            <Image
              source={require('../images/cartao.png')}
              style={{ width: 60, height: 60 }}
            />
          </Pressable>
          <Pressable onPress={() => console.log("TRANSFERENCIA CLICADO")}>
            <Image
              source={require('../images/transferencia-bancaria.png')}
              style={{ width: 60, height: 60 }}
            />
          </Pressable>
        </View>
        </View>
        {/* <View style={styles.container}>
          <Menu />
        </View> */}
      </>
    );
  };

  // return (
  //   <View style={styles.container}>
  //     <Menu />
  //   </View>
  // );
