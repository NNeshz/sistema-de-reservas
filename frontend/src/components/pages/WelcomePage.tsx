import Link from "next/link";
import MaxWidthWrapper from "../MaxWidthWrapper";
import Image from "next/image";
import { buttonVariants } from "../ui/button";
import { cn } from "@/lib/utils";

const WelcomePage = () => {
  return (
    <div className="h-screen w-full flex justify-center items-center">
      <MaxWidthWrapper className="w-full h-full flex flex-col md:flex-row items-center px-8">
        <section className="flex flex-col justify-center md:w-1/2 h-1/2 md:h-full">
          <h3 className="text-4xl font-bold">
            Bienvenido a nuestro Restaurant
          </h3>
          <p className="mt-4 md:pr-4">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Asperiores
            facilis assumenda in corrupti dolorum sequi voluptatum rerum tempora
            inventore libero unde dignissimos non eligendi enim, aut neque!
            Eligendi nulla maiores odio ea, sunt numquam cupiditate similique
            corrupti ipsa reiciendis nostrum laudantium? Harum cupiditate
            aliquam eligendi!
          </p>
          <Link
            href={"/reservaciones"}
            className={cn(
              "mt-4",
              buttonVariants({
                variant: "default",
                className: "w-52",
              })
            )}
          >
            ¡Reservar una mesa ahora!
          </Link>
        </section>
        <section className="w-full md:w-1/2 h-1/2 md:h-full relative rounded-lg">
          <Image
            alt="Food"
            src="https://images.unsplash.com/photo-1589270018935-ae7e307e79b6?q=80&w=1688&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            layout="fill"
            objectFit="cover"
            quality={80}
            className="p-4 md:py-32 rounded-lg"
          />
        </section>
      </MaxWidthWrapper>
    </div>
  );
};

export default WelcomePage;
