// Import Firebase modules
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-firestore.js";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyD39N626JBDn5d5lk6mLHc82DNCF4aEAgc",
    authDomain: "project-c6b15.firebaseapp.com",
    projectId: "project-c6b15",
    storageBucket: "project-c6b15.firebasestorage.app",
    messagingSenderId: "370167031967",
    appId: "1:370167031967:web:1849f3c656aa3c557cdaaa",
    measurementId: "G-T12FQ6XYNZ"
  };
// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Handle Form Submission
document.getElementById('contactForm').addEventListener('submit', async (event) => {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    try {
        // Save to Firestore
        await addDoc(collection(db, "contacts"), {
            name,
            email,
            message,
            createdAt: new Date()
        });

        alert('Message sent successfully!');
        document.getElementById('contactForm').reset();
    } catch (error) {
        console.error('Error submitting contact form:', error);
        alert('Failed to send message. Please try again.');
    }
});
