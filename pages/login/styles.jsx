import {StyleSheet} from 'react-native'

const styles = StyleSheet.create({
    container:{
        backgroundColor:'#D6D6B1',
        alignItems:'center',
        justifyContent:'center',
        flex:1,
    },
    caixa:{
        width:'80%',
        borderWidth:1,
        borderRadius: 5,
        padding:10,
        fontSize:25,
        backgroundColor:'#E2E2D9',
        marginTop:10,
    },
    title:{
        fontSize: 40,
        fontWeight:'bold'
    },
    caixas:{
        alignItems:'center',
        justifyContent:'center',
        backgroundColor:'#4F181F',
        padding:210,
    },
    btnOk:{
        marginTop:10,
        borderWidth:1,
        borderRadius:10,
        width: 140,
        height:50,
        backgroundColor:'#901F2C',
        alignItems:'center',
        justifyContent:'center',
    },
    box_login:{
        height: 40,
        marginTop: 10,
        padding: 30,
        backgroundColor:'#4F181F',

    },
})

export default styles