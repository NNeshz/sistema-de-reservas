"use client";

import { AspectRatio } from "@radix-ui/react-aspect-ratio";
import { StarFilledIcon } from "@radix-ui/react-icons";
import { StarHalfIcon, StarIcon } from "lucide-react";
import Image from "next/image";
import { Badge } from "./ui/badge";

const TopDish = ({
  name,
  description,
  imgSource,
  price,
  stars,
}: {
  name: string;
  description: string;
  imgSource: string;
  price: number;
  stars: number;
}) => {
  return (
    <div className="col-span-1 w-full p-3 bg-gray-50 rounded-lg">
      <div className="flex items-center justify-between">
        <h4 className="text-2xl font-bold">{name}</h4>

        <span className="flex items-center gap-x-1">
          {stars} <StarFilledIcon className="h-5 w-5 text-yellow-300" />{" "}
        </span>
      </div>
      <section className="w-full flex items-center justify-between mb-2">
        <p >{description}</p>
        <Badge className="w-16 flex justify-center">$ {price}</Badge>
      </section>
      <AspectRatio ratio={1 / 1}>
        <Image
          src={imgSource}
          alt="Dish 1"
          fill
          objectFit="cover"
          quality={100}
          className="rounded-lg"
        />
      </AspectRatio>
    </div>
  );
};

export default TopDish;
