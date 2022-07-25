import { configureStore } from '@reduxjs/toolkit';
import userReducer from '../containers/auth/authSlice';

export const store = configureStore({
  reducer: {
    user: userReducer
  },
});
