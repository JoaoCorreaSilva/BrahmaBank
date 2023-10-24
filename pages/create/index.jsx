import React, { useState, useEffect } from 'react'
import { View, Text, TouchableOpacity, TextInput, Image } from 'react-native'
import styles from './styles'
import { db, storage } from '../firebaseConfig'
import { collection, addDoc } from 'firebase/firestore'
import { ref, uploadBytesResumable } from 'firebase/storage'
import * as DocumentPicker from 'expo-document-picker';


export default function Create({ navigation }) {
    const [texto, setTexto] = useState('')
    const [nome, setNome] = useState('')
    const [email, setEmail] = useState('')
    const [imagem, setImagem] = useState('')
    const [imgUrl, setImgUrl] = useState('')
    const [preview, setPreview] = useState(require('../../assets/icon.png'))

    //############## Imagem ##################
    useEffect(() => {
        if (!imagem) {
            setPreview(require('../../assets/icon.png'))
            return
        }

        const objectUrl = URL.createObjectURL(imagem)
        setPreview(objectUrl)

        return () => URL.revokeObjectURL(objectUrl)
    }, [imagem])
    //############# Fim Imagem ###############

    const upload = () => {
        console.log(objectUrl)

        const file = imagem

        if (!file) {
            console.log('Faltou imagem...')
            return
        }

        if (!nome) {
            console.log('Faltou nome...')
            return
        }

        if (!email) {
            console.log('Faltou email...')
            return
        }

        if (imagem == null) return

        const storageRef = ref(
            storage,
            `images/${nome.replace(/ +/g, '') + '_' + imagem.name}`
        )

        const uploadTask = uploadBytesResumable(storageRef, file)

        uploadTask.on('state_changed', snapshot => { })

        adicionar()
    }

    async function adicionar() {
        await addDoc(collection(db, 'alunos'), {
            name: nome,
            email: email,
            status: false,
            image: nome.replace(/ +/g, '') + '_' + imagem.name
        })
        setEmail('')
        setNome('')
        setPreview(require('../../assets/icon.png'))
        setTexto('Cadastrado com sucesso!')
    }


    return (
        <View style={styles.container}>
            <View>
                <Text style={styles.txt}>Create</Text>
            </View>
            <View style={styles.foto}>
                <Image source={preview} style={styles.foto1} />
            </View>
            <View>
                <TouchableOpacity
                    style={styles.btn}
                    onPress={(e) => setImagem(DocumentPicker.getDocumentAsync(File, e.target.files[0]))}
                    //https://docs.expo.dev/versions/latest/sdk/document-picker/#documentpickeroptions
                    //(e)=>{setImagem(e.target.files[0])}
                >
                    <Text style={{ fontWeight: 'bold' }}>Imagem</Text>
                </TouchableOpacity>
            </View>

            <View>
                <TextInput
                    style={styles.caixa1}
                    placeholder='Nome'
                    value={nome}
                    onChangeText={(e) => setNome(e)}
                />
            </View>
            <View>
                <TextInput
                    style={styles.caixa1}
                    placeholder='Email'
                    value={email}
                    onChangeText={(e) => setEmail(e)}
                />
            </View>
            <View>
                <TouchableOpacity
                    style={styles.btn}
                    onPress={upload}
                >
                    <Text style={{ fontWeight: 'bold' }}>Criar</Text>
                </TouchableOpacity>
            </View>
            <Text>{texto}</Text>
        </View>
    )
}
