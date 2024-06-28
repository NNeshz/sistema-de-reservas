"use client";

import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "./ui/form";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { Card, CardDescription, CardTitle } from "./ui/card";
import { useRouter } from "next/navigation";
import useUserStore from "@/context/useUserStore";

const signInFormSchema = z.object({
  username: z.string().min(3).max(20),
  password: z.string().min(6),
});

const SignIn = () => {

  const fetchLogin = useUserStore((state) => state.login);
  const isLoggedIn = useUserStore((state) => state.isLoggedIn);
  const router = useRouter();

  const form = useForm<z.infer<typeof signInFormSchema>>({
    resolver: zodResolver(signInFormSchema),
    defaultValues: {
      username: "",
      password: "",
    },
  });

  async function onSubmit(data: z.infer<typeof signInFormSchema>) {
    try {
      await fetchLogin(data);
      if(isLoggedIn) {
        router.push("/");
        router.refresh();
      }
    } catch (error) {
      console.log("Error:", error);
    }
  }

  return (
    <Card className="px-4 py-3">
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-2">
          <CardTitle className="font-semibold">
            Sign in to your account
          </CardTitle>
          <CardDescription className="">
            Enter your username and password to sign in to your account.{" "}
            <strong className="text-primary">Is nice to see you again!</strong>
          </CardDescription>
          <FormField
            control={form.control}
            name="username"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Username</FormLabel>
                <FormControl>
                  <Input placeholder="ExalGithub" {...field} />
                </FormControl>
                <FormDescription>
                  Must be between 3 and 20 characters.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={form.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input type="password" {...field} />
                </FormControl>
                <FormDescription>
                  Must be at least 6 characters.
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <Button type="submit" className="w-full">
            Submit
          </Button>
        </form>
      </Form>
    </Card>
  );
};

export default SignIn;
