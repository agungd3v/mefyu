import { useState } from "react";
import Image from "next/image";
import TextareaAutosize from "react-textarea-autosize";

export default function CardContent() {
  const [comment, setComment] = useState<string>("");

  const handleComment = (evt: any) => {
    setComment(evt.target.value);
  }

  return (
    <div className="rounded-lg shadow-sm bg-white overflow-hidden">
      <div className="px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="flex justify-center items-center w-10 h-10 rounded-full border bg-gray-200">
            <Image src={"/icons/person.svg"} width={24} height={24} alt="person" />
          </div>
          <div className="flex flex-col">
            <span className="text-sm font-semibold">Agung Ardiyanto</span>
            <div className="flex gap-1">
              <span className="text-xs text-gray-400">10 jam</span>
              <Image src={"/icons/globe.svg"} width={12} height={12} alt="globe" />
            </div>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <div className="cursor-pointer">
            <Image src={"/icons/kebab-horizontal.svg"} width={22} height={22} alt="" />
          </div>
          <div className="cursor-pointer">
            <Image src={"/icons/x.svg"} width={26} height={26} alt="" />
          </div>
        </div>
      </div>
      <div className="">
        <Image src={"/images/test.jpg"} width={300} height={300} className="w-full" alt="post" />
      </div>
      {/* someone like */}
      <div className="border-b px-4"></div>
      {/* end someone like */}
      <div className="border-b py-3 flex items-center justify-around">
        <div className="flex items-center gap-1">
          <Image src={"/icons/thumbsup.svg"} width={18} height={18} alt="like" />
          <span className="text-xs font-semibold text-gray-400 leading-3">Suka</span>
        </div>
        <div className="flex items-center gap-1">
          <Image src={"/icons/comment.svg"} width={18} height={18} alt="like" />
          <span className="text-xs font-semibold text-gray-400 leading-3">Komentari</span>
        </div>
        <div className="flex items-center gap-1">
          <Image src={"/icons/versions.svg"} width={18} height={18} alt="like" />
          <span className="text-xs font-semibold text-gray-400 leading-3">Bagikan</span>
        </div>
      </div>
      <div className="px-4 py-2 flex items-start gap-2">
        <div className="flex justify-center items-center w-8 h-8 rounded-full border bg-gray-200">
          <Image src={"/icons/person.svg"} width={18} height={18} alt="person" />
        </div>
        <form className="flex-1">
          <div className="w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
            <div className="p-2 pb-0 rounded-t-lg bg-gray-50">
              <label className="sr-only">Your comment</label>
              <TextareaAutosize
                className="w-full text-xs border-0 py-0 px-1 bg-transparent"
                placeholder="Tulis komentar..."
                value={comment}
                onChange={(evt) => handleComment(evt)}
              />
            </div>
            <div className="flex items-center justify-between px-3 pb-2 dark:border-gray-600">
              <div></div>
              <button type="submit" className="inline-flex items-center text-xs font-medium text-center">
                <Image src={"/icons/paper-airplane.svg"} width={16} height={16} alt="" />
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  )
}