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
import { fetchRegister } from "@/utils/auth";
import { useRouter } from "next/navigation";

const signUpFormSchema = z.object({
  username: z.string().min(3).max(20),
  password: z.string().min(6),
});

const SignUp = () => {

  const router = useRouter();

  const form = useForm<z.infer<typeof signUpFormSchema>>({
    resolver: zodResolver(signUpFormSchema),
    defaultValues: {
      username: "",
      password: "",
    },
  });

  async function onSubmit(data: z.infer<typeof signUpFormSchema>) {
    try {
      let response = await fetchRegister(data.username, data.password);
      if(response?.ok) {
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
            Sign up to a new account
          </CardTitle>
          <CardDescription className="">
            Enter your username and password to sign in to your account.{" "}
            <strong className="text-primary">Will be nice to have you!</strong>
          </CardDescription>
          <FormField
            control={form.control}
            name="username"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Username</FormLabel>
                <FormControl>
                  <Input placeholder="NNeshz" {...field} />
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

export default SignUp;
