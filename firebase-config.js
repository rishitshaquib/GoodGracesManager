/*
  Paste your Firebase web app config here.
  Firebase console > Project settings (gear icon) > General > Your apps > Web app > SDK setup and configuration > Config.

  These values are not secrets. They identify your project, and the Firestore rules
  in firestore.rules are what control who can read and write.
  Leave the PASTE values in place to run the site in browser-only mode (data saves to that one browser).
*/
window.FIREBASE_CONFIG = {
  apiKey: "PASTE_API_KEY",
  authDomain: "PASTE_PROJECT_ID.firebaseapp.com",
  projectId: "PASTE_PROJECT_ID",
  storageBucket: "PASTE_PROJECT_ID.firebasestorage.app",
  messagingSenderId: "PASTE_SENDER_ID",
  appId: "PASTE_APP_ID"
};
