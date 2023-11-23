import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';
import styles from './styles';

export default function Home({ navigation, route }) {
  const [cont, setCont] = useState(0);

  const Menu = () => {
    return (
      <View style={styles.cima}>
        <View>
        <Icon name="user" size={40} color="black" />
        </View>
         <Text>Olá Paula</Text>
      </View>
    );
  };

  return (
    <View style={styles.container}>
      <Menu />
    </View>
  );
}
