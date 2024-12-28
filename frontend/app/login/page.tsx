import React from 'react';
import LoginForm from '../_components/login';

const LoginPage = () => {
  return (
    <div className="w-full h-screen grid grid-cols-2">
      <div className="bg-gray-800 text-white flex items-center justify-center">
        <h1 className="text-4xl font-bold">Welcome Back!</h1>
      </div>

      <div className="bg-white flex items-center justify-center">
        <LoginForm />
      </div>
    </div>
  );
};

export default LoginPage;
