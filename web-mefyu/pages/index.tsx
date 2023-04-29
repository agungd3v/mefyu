import CardContent from "@/components/CardContent";

export default function Home() {
  return (
    <div className="w-full flex flex-wrap items-center justify-between mx-auto p-4 md:w-3/6 lg:w-2/6">
      <div className="flex flex-col gap-4 w-full">
        {[...Array(3)].fill(undefined).map((x: any, i: number) => {
          return <CardContent key={i} />
        })}
      </div>
    </div>
  )
}
