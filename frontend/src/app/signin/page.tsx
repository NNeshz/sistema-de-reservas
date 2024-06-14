"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import Link from "next/link";
import { authenticate } from "../actions";

const formSchema = z.object({
  username: z.string().min(3).max(20),
  password: z.string().min(8),
});

export default function ProfileLogin() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
      password: "",
    },
  });

  function onSubmit(values: z.infer<typeof formSchema>) {
    const { username, password } = values;
    authenticate(null, username, password);

    console.log(values);
  }

  return (
    <div className="w-full flex items-center justify-center h-screen">
      <div className="bg-white p-5 shadow-xl rounded-xl">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
            <h3 className="text-2xl font-semibold">¡Bienvenido de vuelta!</h3>
            <FormField
              control={form.control}
              name="username"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Usuario</FormLabel>
                  <FormControl>
                    <Input
                      placeholder="Escribe tu nombre de usuario"
                      {...field}
                    />
                  </FormControl>
                  <FormDescription>
                    Tu nombre de usuario debe tener entre 3 y 20 caracteres.
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
                  <FormLabel>Contraseña</FormLabel>
                  <FormControl>
                    <Input placeholder="Escribe tu una contraseña" {...field} />
                  </FormControl>
                  <FormDescription>
                    Tu contraseña debe tener al menos 8 caracteres.
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
            <Button type="submit" className="w-full font-semibold">Enviar</Button>
            <p className="text-sm">¿Todavía no tienes una cuenta? <Link href={"/signup"} className="text-yellow-400">Registrate</Link> </p>
          </form>
        </Form>
      </div>
    </div>
  );
}
