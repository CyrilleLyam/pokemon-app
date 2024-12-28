"use client";

import React, { FormEvent, useState } from "react";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { API_ENDPOINTS } from "@/constants/api-endpoint";
import { useRouter } from "next/navigation";

const LoginForm = () => {
  const [email, setEmail] = useState("seanglay.sq@outlook.com");
  const [password, setPassword] = useState("seanglaypassword");
  const [loading, setLoading] = useState(false);
  const router = useRouter();


  const login = async (event : FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (loading) return;

    setLoading(true);

    try {
      const response = await fetch(`${API_ENDPOINTS.BASE_URL}${API_ENDPOINTS.LOGIN}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
        credentials: "include"
      });
      const data = await response.json();

      if (response.ok) {
        toast.success("Login successful! Welcome back!");
        setEmail("");
        setPassword("");
        router.push("/dashboard/overview");
      } else {
        toast.error(data.message || "Login failed. Please try again.");
      }
    } catch (error) {
      toast.error("An unexpected error occurred. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md p-8 shadow-lg rounded-lg">
      <h2 className="text-2xl font-bold mb-6 text-gray-800">Login</h2>

      <form onSubmit={login}>
        <div className="mb-4">
          <label htmlFor="email" className="block text-sm font-medium text-gray-600 mb-1">
            Email
          </label>
          <Input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your email"
            className="text-black"
            required
          />
        </div>
        <div className="mb-6">
          <label htmlFor="password" className="block text-sm font-medium text-gray-600 mb-1">
            Password
          </label>
          <Input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            className="text-black"
            required
          />
        </div>
        <Button type="submit" disabled={loading} className="w-full">
          {loading ? (
            <svg
              className="animate-spin h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              ></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
              ></path>
            </svg>
          ) : (
            "Login"
          )}
        </Button>
      </form>
    </div>
  );
};

export default LoginForm;
