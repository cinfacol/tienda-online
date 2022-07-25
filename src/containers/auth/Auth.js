import React from "react"
import { useSelector, useDispatch } from "react-redux"

export function Auth() {
  const user = useSelector(state => state.auth.value)
  const dispatch = useDispatch()

  return (
    <div></div>
  )
}