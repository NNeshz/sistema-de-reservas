import { cn } from "@/lib/utils";

const ReviewCard = ({
  name,
  username,
  body,
  className
}: {
  name: string;
  username: string;
  body: string;
  className?: string;
}) => {
  return (
    <figure
      className={cn(
        "relative w-64 cursor-pointer overflow-hidden rounded-xl border p-4", className)}
    >
      <div className="flex flex-row items-center gap-2">
        <div className="flex flex-col">
          <figcaption className="text-sm font-medium text-primary">
            {name}
          </figcaption>
          <p className="text-xs font-medium">{username}</p>
        </div>
      </div>
      <blockquote className="mt-2 text-sm">{body}</blockquote>
    </figure>
  );
};

export default ReviewCard;