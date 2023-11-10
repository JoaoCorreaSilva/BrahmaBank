import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
import {getStorage} from 'firebase/storage'


const firebaseConfig = {
  apiKey: "AIzaSyBKF6m6SRALiftjDQv435T-NkHJttQ5iUY",
  authDomain: "abacaxi-com-abobora.firebaseapp.com",
  projectId: "abacaxi-com-abobora",
  storageBucket: "abacaxi-com-abobora.appspot.com",
  messagingSenderId: "687356265983",
  appId: "1:687356265983:web:a445d69e12cb7c005813ca"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app)
const auth = getAuth(app);
const storage = getStorage(app)

export {auth, db, storage}